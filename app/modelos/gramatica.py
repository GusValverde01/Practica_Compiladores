import re

class Gramatica:
    def __init__(self, gramatica_texto):
        self.gramatica_texto = gramatica_texto
        self.N = set()
        self.T = set()
        self.P = dict()
        self.S = None
        self.parsear_gramatica()

    def parsear_gramatica(self):
        # Handle BNF format like <S> ::= a<A> | b
        lines = self.gramatica_texto.strip().split('\n')
        for linea in lines:
            if '::=' not in linea:
                continue
            izq, der = [x.strip() for x in linea.split('::=')]
            # Remove angle brackets from non-terminal
            izq = izq.strip('<>')
            if not self.S:
                self.S = izq
            self.N.add(izq)
            producciones = [p.strip() for p in der.split('|')]
            if izq not in self.P:
                self.P[izq] = []
            for prod in producciones:
                # Process each production, handling grouped notations like [a-z]
                symbols = self.parse_production(prod)
                self.P[izq].append(symbols)
        # Detect terminals
        for der in self.P.values():
            for prod in der:
                for simb in prod:
                    if simb not in self.N and simb != 'ε':
                        self.T.add(simb)

    def parse_production(self, prod):
        # Parse a production, expanding grouped notations like [a-z]
        symbols = []
        i = 0
        while i < len(prod):
            if prod[i] == '<':
                # Non-terminal
                end = prod.find('>', i)
                if end == -1:
                    break
                symbols.append(prod[i+1:end])
                i = end + 1
            elif prod[i] == '[':
                # Grouped notation like [a-z] or [0-9]
                end = prod.find(']', i)
                if end == -1:
                    break
                group = prod[i+1:end]
                if '-' in group:
                    start, end_char = group.split('-')
                    if start.isalpha() and end_char.isalpha():
                        # Expand letters, e.g., [a-z]
                        symbols.extend(chr(c) for c in range(ord(start.lower()), ord(end_char.lower()) + 1))
                    elif start.isdigit() and end_char.isdigit():
                        # Expand digits, e.g., [0-9]
                        symbols.extend(str(c) for c in range(int(start), int(end_char) + 1))
                i = end + 1
            else:
                # Single terminal
                if prod[i].strip():
                    symbols.append(prod[i])
                i += 1
        return symbols if symbols else ['ε']  # Empty production is epsilon

    def mostrar_cuadrupla(self):
        return {
            "N": ', '.join(sorted(self.N)),
            "T": ', '.join(sorted(self.T)),
            "P": self.formatear_producciones(self.P),
            "S": self.S
        }

    def formatear_producciones(self, producciones):
        txt = ""
        for izq in producciones:
            derechos = [" ".join(prod) if prod != ['ε'] else "ε" for prod in producciones[izq]]
            txt += f"{izq} -> {' | '.join(derechos)}\n"
        return txt.strip()

    def clasificacion(self):
        es_libre_contexto = True
        es_regular = True

        for izq, derechos in self.P.items():
            if len(izq) > 1:
                es_libre_contexto = False
                es_regular = False
                break
            for derecho in derechos:
                if len(derecho) == 1:
                    if derecho[0] in self.T or derecho[0] == 'ε':
                        continue
                    elif derecho[0] in self.N:
                        continue
                    else:
                        es_regular = False
                        es_libre_contexto = False
                elif len(derecho) == 2:
                    if (derecho[0] in self.T and derecho[1] in self.N) or (derecho[1] in self.T and derecho[0] in self.N):
                        continue
                    else:
                        es_regular = False
                        es_libre_contexto = False
                else:
                    es_regular = False
                    es_libre_contexto = False

        if es_regular:
            return "Tipo 3 (Gramática Regular)"
        elif es_libre_contexto:
            return "Tipo 2 (Gramática Libre de Contexto)"
        else:
            return "No es Tipo 2 ni Tipo 3"

    def simbolos_vivos(self):
        vivos = set()
        while True:
            nuevos = set()
            for izq, derechos in self.P.items():
                for prod in derechos:
                    if all(simb in self.T or simb == 'ε' or simb in vivos for simb in prod):
                        if izq not in vivos:
                            nuevos.add(izq)
            if not nuevos:
                break
            vivos.update(nuevos)
        return vivos

    def simbolos_muertos(self):
        return self.N - self.simbolos_vivos()

    def simbolos_accesibles(self):
        accesibles = set([self.S])
        while True:
            nuevos = set()
            for izq in accesibles.copy():
                for prod in self.P.get(izq, []):
                    for simb in prod:
                        if simb in self.N and simb not in accesibles:
                            nuevos.add(simb)
            if not nuevos:
                break
            accesibles.update(nuevos)
        return accesibles

    def simbolos_inaccesibles(self):
        return self.N - self.simbolos_accesibles()

    def reglas_eliminadas(self):
        vivos = self.simbolos_vivos()
        accesibles = self.simbolos_accesibles()
        limpiar = vivos & accesibles

        reglas_eliminadas = []
        nuevas_P = dict()
        for nt in limpiar:
            prod_limpias = []
            for prod in self.P[nt]:
                if all(x in self.T or x == 'ε' or x in limpiar for x in prod):
                    prod_limpias.append(prod)
                else:
                    reglas_eliminadas.append(f"{nt} -> {' '.join(prod)}")
            if prod_limpias:
                nuevas_P[nt] = prod_limpias

        for nt in (self.N - limpiar):
            for prod in self.P.get(nt, []):
                reglas_eliminadas.append(f"{nt} -> {' '.join(prod)}")
        self.P_limpia = nuevas_P
        self.N_limpia = set(nuevas_P.keys())
        self.T_limpia = set()
        for prods in nuevas_P.values():
            for prod in prods:
                for s in prod:
                    if s not in self.N_limpia and s != 'ε':
                        self.T_limpia.add(s)
        return "\n".join(reglas_eliminadas)

    def mostrar_cuadrupla_final(self):
        self.reglas_eliminadas()
        return {
            "N": ', '.join(sorted(self.N_limpia)),
            "T": ', '.join(sorted(self.T_limpia)),
            "P": self.formatear_producciones(self.P_limpia),
            "S": self.S if self.S in self.N_limpia else (next(iter(self.N_limpia), ""))
        }
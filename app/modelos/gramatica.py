import re

class Gramatica:
    def __init__(self, texto_bnf):
        self.texto_bnf = texto_bnf
        self.N = set()  # No terminales
        self.T = set()  # Terminales
        self.P = []     # Producciones
        self.S = None   # Símbolo inicial
        self._parsear_bnf()

    def _parsear_bnf(self):
        """
        Parsea la gramática en BNF, extrayendo N, T, P, y S.
        """
        lineas = self.texto_bnf.strip().split('\n')
        for i, linea in enumerate(lineas):
            if not linea.strip():
                continue
            # Encontrar no terminal izquierdo: <X>
            match_izq = re.match(r'\s*<\s*([\w\d]+)\s*>\s*::=\s*(.*)', linea)
            if match_izq:
                izquierdo = match_izq.group(1)
                derechos = match_izq.group(2).split('|')
                self.N.add(izquierdo)
                if i == 0:
                    self.S = izquierdo  # El primero es el símbolo inicial
                for d in derechos:
                    prod = d.strip().split()
                    self.P.append((izquierdo, prod))
                    # Rellenar terminales y no terminales de la derecha
                    for simbolo in prod:
                        nt = re.match(r'<\s*([\w\d]+)\s*>', simbolo)
                        if nt:
                            self.N.add(nt.group(1))
                        elif simbolo not in ['|', '', '::=']:
                            self.T.add(simbolo)
            else:
                continue
#Muestra la cuadrupla inicial 
    def mostrar_cuadrupla(self):
        return {
            'N': self.N,
            'T': self.T,
            'P': self.P,
            'S': self.S
        }

    def clasificar_chomsky(self):
        """
        Retorna string indicando el tipo de gramática:
        'Tipo3 (Regular)', 'Tipo 2 (Libre de contextoo)', otra
        """
        es_regular = True
        es_libre_contexto = True

        for izquierdo, derecho in self.P:
            # Solo 1 símbolo en el lado izquierdo para tipo 2/3
            if not (isinstance(izquierdo, str) and izquierdo in self.N):
                es_regular = False
                es_libre_contexto = False
                break

            # Analizar el lado derecho para tipo 3
            if len(derecho) == 0:
                # Producción ε (vacía), aceptable en ambas
                continue

            if len(derecho) == 1:
                if derecho[0] in self.T or derecho[0] == 'ε':
                    continue
                elif derecho[0] in self.N:
                    # <A> ::= <B> (permitido regular a la izquierda SOLO si es epsilon)
                    continue
                else:
                    es_regular = False
            elif len(derecho) == 2:
                # Puede ser a <A> o <A> a (hay gramáticas regulares por la derecha o izquierda)
                if (derecho[0] in self.T and derecho[1] in self.N) or (derecho[1] in self.T and derecho[0] in self.N):
                    continue
                else:
                    es_regular = False
            else:
                es_regular = False

        if es_regular:
            return "Tipo 3 (Gramática Regular)"
        elif es_libre_contexto:
            return "Tipo 2 (Gramática Libre de Contexto)"
        else:
            return "No es Tipo 2 ni Tipo 3"

#Simbolos Vivos y Muertos
    def simbolos_vivos_muertos(self):
        # Vivos: si pueden derivar alguna cadena de terminales
        vivos = set()
        while True:
            nuevos_vivos = set()
            for izquierdo, derecho in self.P:
                if izquierdo in vivos:
                    continue
                # Si todo símbolo en el derecho ya es terminal o vivo, es vivo
                if all(s in self.T or s in vivos or s == 'ε' for s in derecho):
                    nuevos_vivos.add(izquierdo)
            if not nuevos_vivos:
                break
            vivos.update(nuevos_vivos)
        muertos = self.N - vivos
        return vivos, muertos

#Simbolos accesibles e inaccesibles
    def simbolos_accesibles_inaccesibles(self):
        accesibles = set([self.S])
        while True:
            nuevos = set()
            for izq, der in self.P:
                if izq in accesibles:
                    for simbolo in der:
                        if simbolo in self.N and simbolo not in accesibles:
                            nuevos.add(simbolo)
            if not nuevos:
                break
            accesibles.update(nuevos)
        inaccesibles = self.N - accesibles
        return accesibles, inaccesibles

#Metodo para limpiar la gramatica 
#Eliminacion de reglas inecesarias

    def limpiar(self):
        vivos, muertos = self.simbolos_vivos_muertos()
        accesibles, inaccesibles = self.simbolos_accesibles_inaccesibles()

        reglas_limpias = []
        reglas_eliminadas = []

        for izq, der in self.P:
            # Elimina reglas con no terminales muertos o inaccesibles
            if izq not in vivos or izq not in accesibles:
                reglas_eliminadas.append((izq, der))
                continue
            if any(s in muertos or s in inaccesibles for s in der if s in self.N):
                reglas_eliminadas.append((izq, der))
                continue
            # Señala redenominación, pero se eliminan con el siguiente método
            reglas_limpias.append((izq, der))

        self.P = reglas_limpias
        self.N = set(izq for izq, _ in self.P)
        self.T = set(s for _, der in self.P for s in der if s in self.T)

        # -----> Llama aquí a la sustitución de redenominaciones
        eliminadas_redenom = self.eliminar_redenominaciones()
        reglas_eliminadas.extend(eliminadas_redenom)  # mostrar todas las eliminadas

        return reglas_eliminadas


#Sustitucion de reglas de redenominacion 
    def eliminar_redenominaciones(self):
        nuevas_producciones = []
        redenominaciones = {}

        # 1. Encuentra reglas de redenominación A -> B
        for izquierdo, derecho in self.P:
            if len(derecho) == 1 and derecho[0] in self.N:
                # Es una redenominación
                redenominaciones.setdefault(izquierdo, set()).add(derecho[0])
            else:
                nuevas_producciones.append((izquierdo, derecho))

        # 2. Para cada no terminal con redenominaciones, encuentra todas las "herencias" (cierre transitivo)
        for a in list(redenominaciones):
            cola = list(redenominaciones[a])
            while cola:
                b = cola.pop()
                if b in redenominaciones:
                    for c in redenominaciones[b]:
                        if c not in redenominaciones[a]:
                            redenominaciones[a].add(c)
                            cola.append(c)

        # 3. Recomponer las producciones: por cada redenominación A -> B, agrega a A todas las reglas no redenominación de B
        for a, destinos in redenominaciones.items():
            for b in destinos:
                for izq, der in self.P:
                    if izq == b and not (len(der) == 1 and der[0] in self.N):
                        if (a, der) not in nuevas_producciones:
                            nuevas_producciones.append((a, der))

        # 4. Reemplaza las producciones
        previamente = set(self.P)
        ahora = set(nuevas_producciones)
        eliminadas = previamente - ahora

        self.P = nuevas_producciones
        return eliminadas      # Regresa las reglas que fueron eliminadas(op)


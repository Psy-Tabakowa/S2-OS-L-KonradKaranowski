from frames.base_summary import BaseSummary


class SummaryAlg3(BaseSummary):

    title = 'Summary of page replacement'

    message = """
Badanie algorytmów zastępowania stron. 

Należy samodzielnie sformułować założenia symulacji: 

- rozmiar pamięci wirtualnej (ilość stron). 

- rozmiar pamięci fizycznej (ilość ramek). 

- długość (powinna być znaczna - min. 1000) i sposób generowania ciągu odwołań
 do stron (koniecznie uwzględnić zasadę lokalności odwołań).

Działanie programu: 

- wygenerować losowy ciąg n odwołań do stron 

- dla wygenerowanego ciągu podać liczbę błędów strony dla różnych algorytmów 
zastępowania stron: 

1. FIFO (usuwamy stronę najdłużej przebywającą w pamięci fizycznej) 

2. OPT (optymalny - usuwamy stronę, która nie będzie najdłużej używana) 

3. LRU (usuwamy stronę, do której najdłużej nie nastąpiło odwołanie) 

4. aproksymowany LRU (wiadomo) 

5. RAND (usuwamy losowo wybraną stronę) 

- symulacje przeprowadzić (na tym samym ciągu testowym) dla różnej liczby ramek
 (np. kilku (3, 5, 10?) wartości podanych przez użytkownika)

Zakres materiału: wszystko o pamięci wirtualnej (z wykładu)."""

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, controller, **kwargs)
        self.title_place(text=self.title)
        self.create_buttons('alg3_params')
        self.container_place(self.message)

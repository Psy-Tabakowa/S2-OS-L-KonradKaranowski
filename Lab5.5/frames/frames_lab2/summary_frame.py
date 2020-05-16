from frames.base_summary import BaseSummary


class SummaryAlg2(BaseSummary):

    title = 'Summary of access to disk'
    message="""
Symulacja algorytmów planowania dostępu do dysku.
* 'Dysk' to w naszym przypadku liniowo uporządkowany ciąg bloków 
o nr od 1 do MAX.
* Kryterium oceny algorytmów będzie suma przemieszczeń głowicy dysku, 
jak wiadomo proporcjonalna do czasu realizacji zleceń. 
* 1.Sprawdzić algorytmy FCFS, SSTF, SCAN i C-SCAN.
* 2.Następnie założyć, że w systemie istnieją także aplikacje real-time, 
które musza być obsłużone za pomocą EDF i/lub FD-SCAN. Jak wpływa to na wyniki?
UWAGA!
Sformułowanie nie wymienionych powyżej warunków symulacji należy do Państwa. Mam na myśli:
-wielkość 'dysku' (ilość bloków)
-liczba i sposób generowania zgłoszeń (pełna kolejka od początku? zgłoszenia w trakcie? 
rozkład zgłoszeń- równomierny, inny?) 
-sposób uwzględnienia obsługi zgłoszeń real-time
-pozostałe... >>> mile widziana umiejętność uzasadnienia przyjętego rozwiązania."""

    def __init__(self, container, controller, **kwargs):
        super().__init__(container, controller, **kwargs)
        self.title_place(text=self.title)
        self.create_buttons('alg2_params')
        self.container_place(self.message)

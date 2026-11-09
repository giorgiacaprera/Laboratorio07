import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_biblioteche(self):
        """Popola il menu a tendina dei musei."""
        self._view.dropdown_biblioteca.options.clear()
        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(None, "Nessun Filtro"))
        biblioteche = self._model.get_biblioteche()
        if biblioteche:
            for biblioteca in biblioteche:
                self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))
        else:
            self._view.show_alert("Errore nel caricamento delle biblioteche")
        self._view.update()

    def popola_dropdown_genere(self):
        self._view.dropdown_genere.options.clear()
        self._view.dropdown_genere.options.append(ft.dropdown.Option(None, "Nessun Filtro"))
        generi = self._model.get_generi()
        if generi:
            for genere in generi:
                self._view.dropdown_genere.options.append(ft.dropdown.Option(genere))
        else:
            self._view.show_alert("Errore nel caricamento dei generi")
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def on_biblioteca_change(self, e):
        valore = e.control.value
        self.biblioteca_selezionata = None if valore == "Nessun Filtro" else valore

    def on_genere_change(self, e):
        valore = e.control.value
        self.genere_selezionato = None if valore == "Nessun Filtro" else valore


    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        biblioteca = self.biblioteca_selezionata
        genere = self.genere_selezionato

        self._view.lista_libri.controls.clear()
        lista_libri = self._model.get_libri_filtrati(biblioteca, genere)

        if lista_libri is None:
            self._view.show_alert("Errore di connessione al database")
        elif len(lista_libri) == 0:
            self._view.show_alert("Nessun libro trovato")
        else:
            for artefatto in lista_libri:
                self._view.lista_libri.controls.append(ft.Text(f"{libro}"))
        self._view.update()
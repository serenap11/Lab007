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

    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        if biblioteche:
            for b in biblioteche:
                self._view.dd_biblioteca.options.append(ft.dropdown.Option(str(b.nome)))

        generi = self._model.get_generi()
        if generi:
            for g in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(str(g)))

        self._view.dd_biblioteca.on_select = self.seleziona_biblioteca
        self._view.dd_genere.on_select = self.seleziona_genere

    def seleziona_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def seleziona_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    def handle_mostra_libri(self, e):
        biblioteca = self._view.dd_biblioteca.value
        genere = self._view.dd_genere.value
        libri = self._model.get_libri_filtrati(biblioteca, genere)
        self._view.lista_libri.controls.clear()
        if not libri:
            self._view.show_alert("Nessun libro trovato")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(str(libro)))

        self._view.update()


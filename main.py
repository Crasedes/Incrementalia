from textual.app import App
from textual.widgets import Footer, Header, Button, TabPane, TabbedContent, Tree, Label, Input
from textual.containers import VerticalGroup, HorizontalGroup


from explorer import Folder, File


class MainApp(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    def compose(self):

        with TabbedContent():
            with TabPane("Main"):
                yield MainContainer()
                yield Label(id="info")
                yield Label(id="log")


            with TabPane("Explorer test"):
                yield Input(placeholder="Entrez le nom du fichier ou dossier à ajouter", id="contentAddingName")

                yield AddingContentButtons()

                yield Label("")

                dossier_projet = Folder("projet")
                readme = File("readme.md")
                dossier_projet.add(readme)
                dossier_src = Folder("src")
                for nom in ["main.py", "explorer.py"]:
                    fichier_src = File(nom)
                    dossier_src.add(fichier_src)
                dossier_projet.add(dossier_src)
                arbre_projet = dossier_projet.toTree()
                arbre_projet.id = "testTree"
                yield arbre_projet

        yield Header()
        yield Footer()


    def on_tree_node_selected(self, event: Tree.NodeSelected):
            source = event.control.id  

            self.labelInfo.update(f"Clic dans '{source}' sur : {event.node.label} avec la donnée : {event.node.data}")
            self.selectedNode = event.node



    def on_mount(self):
        self.selectedNode = None
        self.labelInfo = self.query_one("#info", Label)
        self.labelLog = self.query_one("#log", Label)
        
    def action_toggle_dark(self):
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"


class MainContainer(HorizontalGroup):
    def compose(self):
        yield Button("Button 1", "warning", id="neuille")
        yield Button("Button 2", "primary", id="caca")

    def on_button_pressed(self, event):
        if event.button.id == "#neuille" : pass


class AddingContentButtons(HorizontalGroup):
    def compose(self):
        folderButton = Button("Ajouter Dossier", id="addFolder", compact=True)
        fileButton = Button("Ajouter Fichier", id="addFile", compact=True)
        yield folderButton
        yield fileButton

    def on_button_pressed(self, event):
        match event.button.id :
            case "addFolder":
                name = self.app.query_one("#contentAddingName", Input).value
                folder = Folder(name)
                self.app.selectedNode.data.add(folder)
                self.app.selectedNode.add(name, folder)

            case "addFile":
                name = self.app.query_one("#contentAddingName", Input).value
                file = File(name)
                self.app.selectedNode.data.add(file)
                self.app.selectedNode.add_leaf(name, file)


if __name__ == "__main__" :
    app = MainApp()
    app.run() 


import csv
import os
import sys
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class PictureCopyApp(App):
    def copy_pictures(self, source_folder, target_folder, csv_file, species):
        # Convert species to lowercase
        csv_file = '"' + csv_file + '"'
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Extract the image name and specie from the CSV row
                image_name = row['Foto']
                image_specie = row['Specie'].lower()  # Convert image_specie to lowercase
                
                # Check if the specie matches any of the desired species
                if image_specie in species.lower():
                    # Construct the path to the picture in the source folder
                    source_path = os.path.join(source_folder, image_name)
                    
                    # Remove 'DCIM' from the source path
                    source_path = source_path.replace('DCIM/', '')
                    
                    # Check if the picture exists in the source folder
                    if os.path.exists(source_path):
                        # Construct the path to copy the picture to in the target folder
                        target_path = os.path.join(target_folder, image_name)
                        
                        # Copy the picture from the source to the target folder
                        shutil.copyfile(source_path, target_path)
                        
                        # Check if the picture was copied successfully
                        if os.path.exists(target_path):
                            self.output_label.text += f"\nPicture '{image_name}' copied and pasted successfully."
                        else:
                            self.output_label.text += f"\nFailed to paste picture '{image_name}'."
                    else:
                        self.output_label.text += f"\nPicture '{image_name}' not found in the source folder."
                else:
                    self.output_label.text += f"\nSkipping picture '{image_name}' as it does not match any of the species '{species}'."
    def copy_button_pressed(self, instance):
        source_folder = self.source_input.text
        target_folder = self.target_input.text
        csv_file = self.csv_input.text
        species = self.species_input.text
        
        self.copy_pictures(source_folder, target_folder, csv_file, species)

    def build(self):
        # Layout
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Source Folder Input
        self.source_input = TextInput(text='', hint_text='Source Folder')
        layout.add_widget(self.source_input)

        # Target Folder Input
        self.target_input = TextInput(text='', hint_text='Target Folder')
        layout.add_widget(self.target_input)

        # CSV File Input
        self.csv_input = TextInput(text='', hint_text='CSV File')
        layout.add_widget(self.csv_input)

        # Species Input
        self.species_input = TextInput(text='', hint_text='Species (only one)')
        layout.add_widget(self.species_input)

        # Copy Button
        copy_button = Button(text='Copy Pictures')
        copy_button.bind(on_press=self.copy_button_pressed)
        layout.add_widget(copy_button)

        # Output Label
        self.output_label = Label(text='')
        layout.add_widget(self.output_label)

        return layout

if __name__ == '__main__':
    PictureCopyApp().run()
# if __name__ == "__main__":
#     # Check if correct number of arguments are provided
#     if len(sys.argv) < 5:
#         print("Usage: python main.py <copy_from_folder> <paste_to_folder> <csv_file> <specie>")
#         sys.exit(1)
    
#     # Extract command-line arguments
#     source_folder = sys.argv[1]
#     target_folder = sys.argv[2]
#     picture_names_csv = sys.argv[3]
#     species = sys.argv[4]

#     copy_pictures(source_folder, target_folder, picture_names_csv, species)

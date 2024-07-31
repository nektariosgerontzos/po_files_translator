import polib
import pandas as pd
from googletrans import Translator


# The following script takes a .po file and translates it to the desired language
# po_path: The po's file path
# path_to_save: The path for the new .po translated file to be saved
# src_lang: Original language of the initial .po file
# dest_lang: The desired language for the file to be translated 

def translate(po_path, path_to_save, src_lang, dest_lang):
    po_file = polib.pofile(po_path)

    print(f"Project: {po_file.metadata['Project-Id-Version']}")
    print(f"Report-Msgid-Bugs-To: {po_file.metadata['Report-Msgid-Bugs-To']}")
    print(f"POT-Creation-Date: {po_file.metadata['POT-Creation-Date']}")
    print(f"PO-Revision-Date: {po_file.metadata['PO-Revision-Date']}")
    print(f"Language: {po_file.metadata['Language']}")
    print(f"Language-Team: {po_file.metadata['Language-Team']}")
    print(f"Last-Translator: {po_file.metadata['Last-Translator']}")
    print(f"Plural-Forms: {po_file.metadata['Plural-Forms']}")


    translator = Translator()

    new_po = polib.POFile()

    new_po.metadata = po_file.metadata

    for entry in po_file:
        print(f"msgid: {entry.msgid}")
        translated = translator.translate(f"{entry.msgid}", src=src_lang, dest=dest_lang)
        print(f"msgstr: {str(translated.text)}")
        
        add_row = polib.POEntry(msgid=entry.msgid, msgstr=str(translated.text))

        new_po.append(add_row)


    new_po.save(path_to_save)


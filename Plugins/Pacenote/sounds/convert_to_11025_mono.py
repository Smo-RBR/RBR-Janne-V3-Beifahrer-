import argparse
import subprocess
import os

def convert_to_mono(source_dir):
    # Zielverzeichnis bestimmen
    target_dir = os.path.join(source_dir, "mono-11025")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Durch das Verzeichnis gehen und alle Dateien konvertieren
    for file in os.listdir(source_dir):
        # Vollständiger Pfad zur Quelldatei
        source_file = os.path.join(source_dir, file)
        
        # Überprüfe, ob es sich um eine Datei handelt
        if os.path.isfile(source_file):
            # Bestimme den Dateinamen ohne Endung für die Ausgabedatei
            filename_without_ext = os.path.splitext(file)[0]
            output_file = os.path.join(target_dir, f"{filename_without_ext}.ogg")
            
            # FFmpeg-Befehl zum Konvertieren der Datei
            ffmpeg_command = [
                "ffmpeg",
                "-i", source_file,  # Quelldatei
                "-ac", "1",  # Setze den Audiokanal auf 1 für Mono
                "-ar", "11025",  # Setze die Abtastrate auf 11025 Hz
                "-y",  # Überschreibe vorhandene Dateien ohne Nachfrage
                output_file  # Ausgabedatei
            ]
            
            # Führe den FFmpeg-Befehl aus
            subprocess.run(ffmpeg_command)

# ArgumentParser einrichten, um das Verzeichnis über die Befehlszeile zu erhalten
parser = argparse.ArgumentParser(description='Konvertiere alle Audio-Dateien in einem Verzeichnis zu Mono 11025 Hz.')
parser.add_argument('-d', '--directory', type=str, help='Pfad zum Quellverzeichnis', required=True)

args = parser.parse_args()

# Konvertierungsfunktion aufrufen
convert_to_mono(args.directory)

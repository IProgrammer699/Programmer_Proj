import subprocess

print("By Leon Witzke")
print("2026. No Copyright")

def get_usb_devices():
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        """
        Get-CimInstance Win32_PnPEntity |
        Where-Object { $_.PNPDeviceID -like 'USB*' } |
        Select-Object Name, DeviceID, Manufacturer |
        ConvertTo-Json -Compress
        """
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        print("Fehler beim Abrufen der USB-Geräte:")
        print(result.stderr)
        return []

    if not result.stdout.strip():
        return []

    import json

    data = json.loads(result.stdout)

    # Bei nur einem Gerät liefert PowerShell ein Objekt statt einer Liste.
    if isinstance(data, dict):
        data = [data]

    return data


def main():
    print("=" * 60)
    print("           ANGESCHLOSSENE USB-GERÄTE")
    print("=" * 60)

    devices = get_usb_devices()

    if not devices:
        print("\nKeine USB-Geräte gefunden.")
        return

    for number, device in enumerate(devices, start=1):
        print(f"\n[{number}]")
        print(f"  Name:        {device.get('Name', 'Unbekannt')}")
        print(f"  Hersteller:  {device.get('Manufacturer', 'Unbekannt')}")
        print(f"  Device-ID:   {device.get('DeviceID', 'Unbekannt')}")

    print("\n" + "=" * 60)
    print(f"Anzahl gefundener Geräte: {len(devices)}")
    print("=" * 60)


if __name__ == "__main__":
    main()



    print("wenn du ein Gerät ert nach Öffnung des")
    print("anschliest, Starte bitte das Programm Neu.")



    input()
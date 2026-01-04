def update_readme(trending):
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = ""
        end_marker = ""

        start_pos = content.find(start_marker)
        end_pos = content.find(end_marker)

        if start_pos != -1 and end_pos != -1:
            # Összeállítjuk az új listát szövegként
            new_text = "\n".join([f"- {item}" for item in trending])
            
            new_content = (
                content[:start_pos + len(start_marker)] + 
                "\n\n" + new_text + "\n\n" + 
                content[end_pos:]
            )
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
            print("README sikeresen frissítve!")
        else:
            print("Hiba: Markerek nem találhatók a README-ben!")
    except Exception as e:
        print(f"Hiba történt: {e}")

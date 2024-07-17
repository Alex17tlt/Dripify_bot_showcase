from .variables import browser, By, sleep, sheet
import gspread, gspread_formatting

def write_to_sheet(sentiment, scraped_data):

    if sentiment == 'not interested':

        # insert NO at index 3
        scraped_data[0].insert(3, "NO")

        while True:
            try:
                last_row = len(sheet.col_values(col=1)) + 1
                sheet.update(f'A{last_row}:M{last_row}', scraped_data)

                break
            except Exception as e:

                print(str(e))
                sleep(5)

    else:

        # insert Yes at index 3 and color the row green
        scraped_data[0].insert(3, "YES")

        # a reply after our contacts request, color the message cell in green
        while True:
            try:
                last_row = len(sheet.col_values(col=1)) + 1
                sheet.update(f'A{last_row}:M{last_row}', scraped_data)

                gspread_formatting.format_cell_range(sheet,
                                                     f"A{last_row}:K{last_row}",
                                                     cell_format=gspread_formatting.CellFormat(
                                                         backgroundColor=gspread_formatting.Color(0, 1, 0)))

                break
            except Exception as e:

                print(str(e))
                sleep(5)
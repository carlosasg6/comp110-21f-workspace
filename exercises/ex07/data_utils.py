"""Utility functions."""

__author__ = "730330989"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
   
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    column: str = ""
    for column in table:
        lista: list[str] = list()
        i: int = 0
        if num > len(table[column]):
            return table
        while i < num:
            lista.append(table[column][i])
            i += 1
        result[column] = lista
    return result


def select(table: dict[str, list[str]], lista: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for items in lista:
        result[items] = table[items]
    return result


def concat(table_uno: dict[str, list[str]], table_dos: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_uno:
        result[column] = table_uno[column]
    for column in table_dos:
        if column in result[column]:
            result[column] = result[column] + table_dos[column]
        else:
            result[column] = table_dos[column]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Returns a dictionary with with counts of items in the input list."""
    empty: dict[str, int] = {}
    count: str = ""
    for count in a:
        if count in empty:
            empty[count] += 1
        else:
            empty[count] = 1
    return empty
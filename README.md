# Election Results Calculator

This Python script is designed to calculate election results based on the D'Hondt method. It takes into account the number of seats (curules) to be allocated and the number of votes each political party received.

## Usage

1. Modify the `CURULES` variable to specify the total number of seats to be allocated.

2. Define the list of political parties and their respective vote counts in the `PARTIDOS` list. You can add as many parties as needed by appending new dictionary entries to the list.

3. Run the script.

4. The script will calculate the allocation of seats to each party based on the D'Hondt method and display the winning parties.

5. You can also interactively input a desired seat (curul) and the number of votes obtained by a specific party. The script will inform you of the additional votes required to secure that seat.

## Example

Suppose you have 18 seats (CURULES) to allocate and the following parties:

```python
PARTIDOS = [
    {'partido': 'Party A', 'votos': 10000},
    {'partido': 'Party B', 'votos': 7500},
    {'partido': 'Party C', 'votos': 6000},
    # Add more parties here
]

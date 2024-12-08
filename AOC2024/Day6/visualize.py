import json

# Function to generate HTML file for visualization
def generate_html(map_states):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Visualization</title>
    <style>
        body {{
            font-family: monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }}
        .grid {{
            display: grid;
            gap: 2px;
        }}
        .cell {{
            width: 20px;
            height: 20px;
            text-align: center;
            line-height: 20px;
            border: 1px solid #ccc;
            font-size: 12px;
            background-color: white;
        }}
        .cell.obstacle {{ background-color: black; color: white; }}
        .cell.visited {{ background-color: #d1e7dd; }}
        .cell.guard {{ background-color: #ffc107; font-weight: bold; }}
        .controls {{
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div id="grid" class="grid"></div>
    <div class="controls">
        <button id="start">Start</button>
        <button id="pause">Pause</button>
        <button id="reset">Reset</button>
    </div>
    <script>
        const mapStates = {json.dumps(map_states)}; // Insert JSON from Python
        const gridElement = document.getElementById("grid");
        let currentStep = 0;
        let interval;

        function renderMap(map) {{
    gridElement.innerHTML = '';
    const rows = map.length; // Number of rows in the grid
    const cols = map[0].length; // Number of columns in the grid
    gridElement.style.gridTemplateColumns = `repeat(${{cols}}, 1fr)`; // Adjust columns dynamically
    map.forEach(row => {{
        row.forEach(cell => {{
            const div = document.createElement("div");
            div.className = "cell";
            if (cell === "#") div.classList.add("obstacle");
            if (cell === "X") div.classList.add("visited");
            if (["^", ">", "v", "<"].includes(cell)) div.classList.add("guard");
            div.textContent = cell;
            gridElement.appendChild(div);
        }});
    }});
}}


        function startVisualization() {{
            interval = setInterval(() => {{
                if (currentStep < mapStates.length) {{
                    renderMap(mapStates[currentStep]);
                    currentStep++;
                }} else {{
                    clearInterval(interval); // Stop when all steps are displayed
                }}
            }}, 500); // Adjust speed (milliseconds per step)
        }}

        function pauseVisualization() {{
            clearInterval(interval);
        }}

        function resetVisualization() {{
            clearInterval(interval);
            currentStep = 0;
            renderMap(mapStates[0]);
        }}

        document.getElementById("start").addEventListener("click", startVisualization);
        document.getElementById("pause").addEventListener("click", pauseVisualization);
        document.getElementById("reset").addEventListener("click", resetVisualization);

        // Initialize grid with the first state
        renderMap(mapStates[0]);
    </script>
</body>
</html>
"""
    with open("Day6/grid_visualization.html", "w") as file:
        file.write(html_content)


# Usage Example:
map_states = []
# generate_html(map_states)

def capture_map_state(grid):
    map_states.append([row.copy() for row in grid])

# Call this after every movement step
# capture_map_state(map)

# At the end of the simulation, generate the HTML
# generate_html(map_states)

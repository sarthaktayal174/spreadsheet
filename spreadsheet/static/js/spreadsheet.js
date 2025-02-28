document.addEventListener("DOMContentLoaded", function () {
    $('#spreadsheet').DataTable();  // Initialize DataTable

    document.querySelectorAll("#spreadsheet td").forEach(cell => {
        cell.addEventListener("input", function () {
            updateCell(cell);
        });
    });
});

function updateCell(cell) {
    let cellId = cell.getAttribute("data-cell-id");
    let newValue = cell.innerText;

    fetch(`/api/cells/${cellId}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value: newValue })
    })
    .then(response => response.json())
    .then(data => console.log("Updated:", data))
    .catch(error => console.error("Error:", error));
}

function saveSpreadsheet() {
    fetch("/api/spreadsheets/1/save_spreadsheet/")
    .then(response => response.json())
    .then(data => alert("Spreadsheet saved!"))
    .catch(error => console.error("Error:", error));
}

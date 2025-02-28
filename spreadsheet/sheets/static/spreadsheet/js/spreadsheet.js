$(document).ready(function () {
    let table = $('#spreadsheet-table').DataTable({
        paging: false,
        searching: false,
        ordering: false,
        info: false,
        autoWidth: false,
        columnDefs: [{ targets: 0, width: "30px" }]
    });

    // Populate initial 10x10 grid
    for (let row = 1; row <= 10; row++) {
        let rowData = [`${row}`];
        for (let col = 1; col <= 10; col++) {
            rowData.push(`<input type="text" data-row="${row}" data-col="${col}" class="cell-input">`);
        }
        table.row.add(rowData).draw(false);
    }

    // Handle cell edits and save to backend
    $('#spreadsheet-table').on('change', '.cell-input', function () {
        let row = $(this).data('row');
        let col = $(this).data('col');
        let value = $(this).val();

        $.ajax({
            url: '/api/cells/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                spreadsheet: 1,  // Assume default spreadsheet ID = 1
                row: row,
                column: col,
                value: value
            }),
            success: function (response) {
                console.log("Cell updated:", response);
            },
            error: function (error) {
                console.error("Error updating cell:", error);
            }
        });
    });

    // Load existing spreadsheet data
    $.get('/api/cells/', function (data) {
        data.forEach(cell => {
            $(`input[data-row="${cell.row}"][data-col="${cell.column}"]`).val(cell.value);
        });
    });
});

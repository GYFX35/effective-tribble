document.addEventListener('DOMContentLoaded', () => {
    const shipmentsTable = document.querySelector('#shipments-table tbody');

    if (shipmentsTable) {
        fetch('/api/shipments')
            .then(response => response.json())
            .then(data => {
                data.forEach(shipment => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${shipment.id}</td>
                        <td>${shipment.origin}</td>
                        <td>${shipment.destination}</td>
                        <td>${shipment.status}</td>
                    `;
                    shipmentsTable.appendChild(row);
                });
            });
    }
});

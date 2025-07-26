async function fetchTransactions() {
    const response = await fetch('http://127.0.0.1:8000/transactions/');
    const data = await response.json();
    const list = document.getElementById('transactions');
    list.innerHTML = '';
    data.forEach(tx => {
        const item = document.createElement('li');
        item.textContent = `#${tx.id}: ${tx.contract.property_address} (Buyer: ${tx.contract.buyer_name}, Seller: ${tx.contract.seller_name})`;
        list.appendChild(item);
    });
}

async function addTransaction(event) {
    event.preventDefault();
    const property = document.getElementById('property').value;
    const buyer = document.getElementById('buyer').value;
    const seller = document.getElementById('seller').value;
    const closing = document.getElementById('closing').value || null;
    const payload = {
        contract: {
            property_address: property,
            buyer_name: buyer,
            seller_name: seller,
            closing_date: closing
        }
    };
    await fetch('http://127.0.0.1:8000/transactions/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
    document.getElementById('transaction-form').reset();
    fetchTransactions();
}

document.getElementById('transaction-form').addEventListener('submit', addTransaction);
// Load existing transactions on page load
fetchTransactions();
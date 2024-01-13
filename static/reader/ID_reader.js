async function initNFC() {
    try {
        const ndef = new NDEFReader();

        ndef.addEventListener('reading', async ({ message }) => {
            console.log('NFC Data:', message);

            // Extract and display text data
            for (const record of message.records) {
                const textDecoder = new TextDecoder();
                const data = textDecoder.decode(record.data);
                console.log('Record Type:', record.recordType);
                console.log('Record Data:', data);

                // Send data to Django backend using form submission
                const response = await sendDataToDjango(record.recordType, data);

                // Redirect to the specified URL after successful data submission
                if (response.success) {
                    const id = response.id; // Assuming the response contains an ID
                    redirectToWebsite(`passenger_tapped/${id}/`);
                }
            }
        });

        await ndef.scan();
        console.log('NFC Reader is ready.');
    } catch (error) {
        console.error('Error initializing NFC:', error);
    }
}

async function sendDataToDjango(recordType, data) {
    try {
        const form = new FormData();
        form.append('record_type', recordType);
        form.append('data', data);

        const response = await fetch('save_nfc_data/', {
            method: 'POST',
            body: form,
        });

        const result = await response.json();
        console.log('Data sent to Django. Server response:', result);

        return result; // Assuming your Django backend sends a JSON response with success and id properties
    } catch (error) {
        console.error('Error sending data to Django:', error);
    }
}

function redirectToWebsite(path) {
    // Redirect to the specified path
    window.location.href = path;
}

// Check if the browser supports the Web NFC API
if ('NDEFReader' in window) {
    initNFC();
} else {
    // Browser does not support Web NFC API
    console.error('Web NFC API is not supported in this browser.');
}

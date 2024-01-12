document.addEventListener('DOMContentLoaded', (event) => {
    const scanButton = document.getElementById('scanButton');

    if ('NDEFReader' in window) {
        // Web NFC API is supported

        scanButton.addEventListener('click', async () => {
            try {
                const ndef = new NDEFReader();
                await ndef.scan();

                ndef.addEventListener('reading', ({ message }) => {
                    // Handle the NFC data
                    console.log('NFC Data:', message);
                    alert('Button 1 clicked!');
                });
                alert('Button 1 clicked!');
                console.log('Scanning for NFC...');
            } catch (error) {
                console.error('Error while scanning for NFC:', error);
            }
        });
    } else {
        // Web NFC API is not supported
        console.error('Web NFC API is not supported in this browser.');
    }
});

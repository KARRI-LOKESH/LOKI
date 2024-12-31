function clearDisplay() {
    document.getElementById('disp').value = '';
}

function deleteLast() {
    const display = document.getElementById('disp');
    display.value = display.value.slice(0, -1);
}

function appendToDisplay(value) {
    const display = document.getElementById('disp');
    if (value === '=') {
        try {
            display.value = eval(display.value);
        } catch (e) {
            display.value = 'Error';
        }
        return;
    }
    display.value += value;
}

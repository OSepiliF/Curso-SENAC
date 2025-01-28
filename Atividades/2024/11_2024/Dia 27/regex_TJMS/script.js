function npuValidate() {
    const npuInput = document.querySelector('.input_npu_required');
    const errorSpan = document.querySelector('.span-required');
    const successSpan = document.querySelector('.span-valid');
    const npu = /^[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.[8]{1}\.[0-9]{2}\.[0-9]{4}$/;

    if (npu.test(npuInput.value)) {
        removeError();
    } else {
        setError();
    }

    function setError() {
        errorSpan.style.display = 'block';
        errorSpan.style.color = 'red';
        successSpan.style.display = 'none';
    }

    function removeError() {
        errorSpan.style.display = 'none';
        successSpan.style.display = 'block';
        successSpan.style.color = 'green';
    }
}
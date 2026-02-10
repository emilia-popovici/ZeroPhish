document.addEventListener('DOMContentLoaded', function() {
    console.log("Main.js a fost încărcat!");
    const formInputs = document.querySelectorAll('.form-control-custom');
    
    if (formInputs.length > 0) {
        const patterns = {
            name: /^[a-zA-ZăâîșțĂÂÎȘȚ\s\-]+$/,
            email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            phone: /^[\d\s]+$/ 
        };

        const prefixSelect = document.querySelector('.prefix-select');
        if (prefixSelect) updatePrefix(prefixSelect);

        formInputs.forEach(input => {
            input.addEventListener('input', function() {
                const group = this.closest('.input-group-custom');
                if (!group) return;

                const button = group.querySelector('button');
                let errorMsg = group.querySelector('.error-msg');
                if (!errorMsg && group.parentElement) {
                    errorMsg = group.parentElement.querySelector('.error-msg');
                }
                
                const originalValue = this.getAttribute('data-original');
                const currentValue = this.value; 
                let isValid = true;

                if (this.classList.contains('validate-name')) {
                    isValid = patterns.name.test(currentValue) && currentValue.trim().length > 1;
                } else if (this.classList.contains('validate-email')) {
                    isValid = patterns.email.test(currentValue.trim());
                } else if (this.classList.contains('validate-phone')) {
                    const cleanPhone = currentValue.replace(/\s/g, ''); 
                    isValid = patterns.phone.test(currentValue) && cleanPhone.length > 5;
                }

                if (!isValid && currentValue.length > 0) {
                    this.classList.add('is-invalid');
                    if (errorMsg) errorMsg.style.display = 'block';
                } else {
                    this.classList.remove('is-invalid');
                    if (errorMsg) errorMsg.style.display = 'none';
                }

                if (button) {
                    const safeOriginal = originalValue ? originalValue.trim() : '';
                    const safeCurrent = currentValue.trim();

                    if (isValid && safeCurrent !== safeOriginal && safeCurrent.length > 0) {
                        console.log("Activare buton pentru:", this.name);
                        button.classList.remove('btn-disabled');
                        button.classList.add('btn-enabled');
                        button.disabled = false;
                        button.style.pointerEvents = "auto";
                    } else {
                        button.classList.remove('btn-enabled');
                        button.classList.add('btn-disabled');
                        button.style.pointerEvents = "none";
                    }
                }
            });
        });
    }
    
    const passError = document.getElementById('passErrorFlag');
    if (passError) {
        const modalElement = document.getElementById('passModal');
        if (modalElement && typeof bootstrap !== 'undefined') {
            const passModal = new bootstrap.Modal(modalElement);
            passModal.show();
        }
    }

    const progressBar = document.getElementById("myBar");
    if (progressBar) {
        window.onscroll = function() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            var scrolled = (winScroll / height) * 100;
            progressBar.style.width = scrolled + "%";
        };
    }
});

window.updatePrefix = function(selectElement) {
    const wrapper = selectElement.closest('.prefix-wrapper');
    const display = wrapper.querySelector('.prefix-display');
    if(display) display.textContent = selectElement.value;
    
    const group = wrapper.closest('.input-group-custom');
    if (group) {
        const phoneInput = group.querySelector('input[name="phone_number"]');
        if (phoneInput) {
            phoneInput.dispatchEvent(new Event('input')); 
        }
    }
};
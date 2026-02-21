function updatePrefix(selectElement) {
    const wrapper = selectElement.closest('.prefix-wrapper');
    if (!wrapper) return;
    const display = wrapper.querySelector('.prefix-display');
    if(display) display.textContent = selectElement.value;
    
    const group = wrapper.closest('.input-group-custom');
    if (group) {
        const phoneInput = group.querySelector('input[name="phone_number"]');
        if (phoneInput) {
            phoneInput.dispatchEvent(new Event('input')); 
        }
    }
}

window.updatePrefix = updatePrefix;

document.addEventListener('DOMContentLoaded', function() {
    const formInputs = document.querySelectorAll('.form-control-custom');
    
    if (formInputs.length > 0) {
        const patterns = {
            name: /^[a-zA-ZăâîșțĂÂÎȘȚ\s\-]+$/,
            email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            phone: /^[\d\s]*$/ 
        };

        const prefixSelect = document.querySelector('.prefix-select');
        if (prefixSelect) updatePrefix(prefixSelect);

        formInputs.forEach(input => {
            input.addEventListener('input', function() {
                const group = this.closest('.input-group-custom');
                if (!group) return;

                const button = group.querySelector('button');
                let errorMsg = group.querySelector('.error-msg') || 
                               (group.parentElement ? group.parentElement.querySelector('.error-msg') : null);
                
                const originalValue = this.getAttribute('data-original') || '';
                const currentValue = this.value; 
                let isValid = true;

                if (currentValue.length > 0) {
                    if (this.classList.contains('validate-name')) {
                        isValid = patterns.name.test(currentValue) && currentValue.trim().length > 1;
                    } else if (this.classList.contains('validate-email')) {
                        isValid = patterns.email.test(currentValue.trim());
                    } else if (this.classList.contains('validate-phone')) {
                        const cleanPhone = currentValue.replace(/\s/g, ''); 
                        isValid = patterns.phone.test(currentValue) && cleanPhone.length > 5;
                    }
                }

                if (!isValid && currentValue.length > 0) {
                    this.classList.add('is-invalid');
                    if (errorMsg) errorMsg.style.display = 'block';
                } else {
                    this.classList.remove('is-invalid');
                    if (errorMsg) errorMsg.style.display = 'none';
                }

                if (button) {
                    const safeOriginal = originalValue.trim();
                    const safeCurrent = currentValue.trim();

                    if (isValid && safeCurrent !== safeOriginal) {
                        button.classList.remove('btn-disabled');
                        button.classList.add('btn-enabled');
                        button.disabled = false;
                        button.style.pointerEvents = "auto";
                    } else {
                        button.classList.remove('btn-enabled');
                        button.classList.add('btn-disabled');
                        button.disabled = true;
                        button.style.pointerEvents = "none";
                    }
                }
            });
        });
    }
    
    const newUsernameInput = document.getElementById('newUsernameInput');
    const saveUserBtn = document.getElementById('saveUserBtn');
    const userErrorMsg = document.getElementById('userErrorMsg');

    if (newUsernameInput && saveUserBtn) {
        newUsernameInput.addEventListener('input', function() {
            const val = this.value.trim();
            const isValid = val.length >= 3;

            if (!isValid && val.length > 0) {
                this.classList.add('is-invalid');
                if (userErrorMsg) userErrorMsg.style.display = 'block';
                saveUserBtn.disabled = true;
                saveUserBtn.classList.add('btn-disabled');
            } else {
                this.classList.remove('is-invalid');
                if (userErrorMsg) userErrorMsg.style.display = 'none';
                if (val.length >= 3) {
                    saveUserBtn.disabled = false;
                    saveUserBtn.classList.remove('btn-disabled');
                } else {
                    saveUserBtn.disabled = true;
                    saveUserBtn.classList.add('btn-disabled');
                }
            }
        });
    }

    const newPassInput = document.getElementById('newPassInput');
    const savePassBtn = document.getElementById('savePassBtn');
    const passErrorMsg = document.getElementById('passErrorMsg');
    const passPattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;

    if (newPassInput && savePassBtn) {
        newPassInput.addEventListener('input', function() {
            const val = this.value;
            const isValid = passPattern.test(val);

            if (!isValid && val.length > 0) {
                this.classList.add('is-invalid');
                if (passErrorMsg) passErrorMsg.style.display = 'block';
                savePassBtn.disabled = true;
                savePassBtn.classList.add('btn-disabled');
            } else {
                this.classList.remove('is-invalid');
                if (passErrorMsg) passErrorMsg.style.display = 'none';
                if (isValid) {
                    savePassBtn.disabled = false;
                    savePassBtn.classList.remove('btn-disabled');
                } else {
                    savePassBtn.disabled = true;
                    savePassBtn.classList.add('btn-disabled');
                }
            }
        });
    }

    if (document.getElementById('passErrorFlag')) {
        const modalElement = document.getElementById('passModal');
        if (modalElement && typeof bootstrap !== 'undefined') {
            new bootstrap.Modal(modalElement).show();
        }
    }

    const progressBar = document.getElementById("myBar");
    if (progressBar) {
        window.addEventListener('scroll', function() {
            var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            if (height > 0) {
                var scrolled = (winScroll / height) * 100;
                progressBar.style.width = scrolled + "%";
            }
        });
    }
});

window.toggleNotifs = function() {
    const menu = document.getElementById('notifMenu');
    menu.classList.toggle('show');
    if (menu.classList.contains('show')) {
        const badge = document.querySelector('.notif-badge');
        if (badge) {
            fetch('/citeste_notificari', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            }).then(response => {
                if (response.ok) {
                    badge.style.display = 'none';
                }
            });
        }
    }
}

document.addEventListener('click', function(event) {
    const container = document.getElementById('notifContainer');
    const menu = document.getElementById('notifMenu');
    if (container && menu && !container.contains(event.target)) {
        menu.classList.remove('show');
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('reserved_share_pct');
    const otherInput = document.getElementById('other-input');

    // Função para atualizar visibilidade
    function updateOtherInput() {
        if (select.value === 'other') {
            otherInput.style.display = 'block';
            otherInput.required = true;
            setTimeout(() => {
                otherInput.focus();
            }, 100);
        } else {
            otherInput.style.display = 'none';
            otherInput.required = false;
        }
    }

    // Inicializa estado
    updateOtherInput();

    // Evento de mudança
    select.addEventListener('change', updateOtherInput);

    // Garantir que o campo "other" seja focado quando ativado
    otherInput.addEventListener('blur', function () {
        if (this.value && this.value < 0) this.value = 0;
        if (this.value && this.value > 100) this.value = 100;
    });
});
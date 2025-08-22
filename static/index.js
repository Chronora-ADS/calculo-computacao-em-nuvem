document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("calc-form");
    const result50 = document.getElementById("result-50");
    const result80 = document.getElementById("result-80");
    const result100 = document.getElementById("result-100");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let custoUnitario = parseFloat(document.getElementById("custo-unitario").value);
        let quantidade = parseInt(document.getElementById("quantidade").value);

        if (isNaN(custoUnitario) || isNaN(quantidade)) {
            alert("Preencha todos os campos corretamente.");
            return;
        }

        let custoTotal = custoUnitario * quantidade;

        result50.textContent = "Cenário 50%: R$ " + (custoTotal * 0.5).toFixed(2);
        result80.textContent = "Cenário 80%: R$ " + (custoTotal * 0.8).toFixed(2);
        result100.textContent = "Cenário 100%: R$ " + custoTotal.toFixed(2);
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // Abrir modais
    document.querySelectorAll('[data-modal-id]').forEach(function(element) {
        element.addEventListener('click', function() {
            var modalId = this.getAttribute('data-modal-id');
            document.getElementById(modalId).style.display = 'block';
        });
    });

    // Fechar modais
    document.querySelectorAll('.close, .btn-cancel').forEach(function(element) {
        element.addEventListener('click', function() {
            var modalId = this.getAttribute('data-modal-id');
            document.getElementById(modalId).style.display = 'none';
        });
    });

    // Fechar ao clicar fora
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal-edit') || event.target.classList.contains('modal-confirm')) {
            event.target.style.display = 'none';
        }
    });
});
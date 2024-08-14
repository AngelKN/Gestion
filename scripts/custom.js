document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#btn-two').addEventListener('click', function () {
        html2canvas(
            document
                .querySelector('iframe')
                .contentWindow.document.querySelector('.receipt-wrap'),
        ).then((canvas) => {
            let base64image = canvas.toDataURL('../img/acciones.png');
            let pdf = new jsPDF('p', 'px', [1600, 1131]);
            pdf.addImage(base64image, 'PNG', 15, 15, 1140, 966);

            // Convertir el PDF a base64 y enviarlo al servidor
            let pdfOutput = pdf.output('datauristring');
            fetch('/save-pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data: pdfOutput }),
            }).then((response) => {
                if (response.ok) {
                    alert('PDF guardado correctamente en la carpeta styles');
                } else {
                    alert('Hubo un problema al guardar el PDF');
                }
            });
        });
    });
});

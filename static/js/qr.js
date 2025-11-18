setTimeout(() => history.replaceState(null, '', window.location.pathname), 150);

async function salvar_com_dialogo() {
    const img = document.getElementById("qr-img");

    const response = await fetch(img.src);
    const blob = await response.blob();

    const handle = await window.showSaveFilePicker({
        suggestedName: "QrcodeK.png",
        types: [
            {
                description: "Arquivo PNG",
                accept: { "image/png": [".png"] }
            }
        ]
    });

    const writable = await handle.createWritable();
    await writable.write(blob);
    await writable.close();

}   
    

function baixar_automatico() {
    const img = document.getElementById("qr-img");
    
    const a = document.createElement("a");
    a.href = img.src;
    a.download = "QrcodeK.png";
    a.click();
}


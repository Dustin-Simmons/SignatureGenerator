function showCorpForm() {
    var x = document.getElementById('corporateForm');
    var z = document.getElementById('retailForm');
    document.getElementById('retailButton').style.backgroundColor='white';
    z.style.display = 'none';
    if (x.style.display === 'none') {
        x.style.display = 'block';
        document.getElementById('corporateButton').style.backgroundColor='#45ad4e';
    }
    // } else {
    //     x.style.display = 'none';
    // }
}

function showRetailForm() {
    var z = document.getElementById('retailForm');
    var x = document.getElementById('corporateForm');
    document.getElementById('corporateButton').style.backgroundColor='white';
    x.style.display = 'none';
    if (z.style.display === 'none') {
        z.style.display = 'block';
        document.getElementById('retailButton').style.backgroundColor='#45ad4e';
    }
    // } else {
    //     z.style.display = 'none';
    // }
}

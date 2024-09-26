const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')

function toggleSidebar() {
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')

    Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
        ul.classList.remove('show')
        ul.previousElementSibling.classList.remove('rotate')
    })
}

function toggleSubMenu(button){
    button.nextElementSibling.classList.toggle('show')
    button.classList.toggle('rotate')

    //untuk mengatasi ketika sidebar ditutup harusnya sidebar menu 
    //tidak dapat dibuka
    if(sidebar.classList.contains('close')){
        sidebar.classList.toggle('close')
        toggleButton.classList.toggle('rotate')
    }
}

document.getElementById('startButton').addEventListener('click', function() {
    const loader = document.getElementById('loader');
    const containerHasil = document.getElementById('containerHasil');
    const containerVideo = document.getElementById('containerVideo'); // Video container
    const popup = document.getElementById('popup'); // Popup element

    // Sembunyikan tombol start
    this.style.display = 'none';
    popup.style.display = 'none';
    

    // Tampilkan loader
    loader.style.display = 'block';

    // Simulasi loader selama 3 detik
    setTimeout(function() {
        loader.style.display = 'none';  // Loader menghilang
        containerHasil.style.display = 'block';  // Tampilkan container-hasil setelah loader selesai
        containerVideo.style.display = 'flex';  // Tampilkan container-video setelah loader selesai
    }, 3000);  // Loader tampil selama 3 detik
});
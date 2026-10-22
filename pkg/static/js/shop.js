const buttons = document.querySelectorAll('.filter-btn');
const cards = document.querySelectorAll('.product-card');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    // 1. change active color
    buttons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.dataset.filter;

    // 2. filter cards
    cards.forEach(card => {
      if(filter === 'All' || card.dataset.category === filter){
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});
document.querySelectorAll('form .state-select').forEach(stateSelect => {
  const locationFields = stateSelect.closest('.location-select-fields');
  const lgaSelect = locationFields?.querySelector('.lga-select');

  if (!lgaSelect) {
    console.error('State select is missing its matching LGA select.');
    return;
  }

  stateSelect.addEventListener('change', async () => {
    const stateId = stateSelect.value;
    lgaSelect.replaceChildren();

    if (!stateId) {
      lgaSelect.add(new Option('Select state first', ''));
      lgaSelect.disabled = true;
      return;
    }

    const lgaUrl = stateSelect.dataset.lgaUrl;
    if (!lgaUrl) {
      console.error('State select is missing its LGA URL.');
      lgaSelect.add(new Option('Could not load LGAs. Please try again.', ''));
      lgaSelect.disabled = true;
      return;
    }

    lgaSelect.add(new Option('Loading...', ''));
    lgaSelect.disabled = true;

    try {
      const url = lgaUrl.replace(/0$/, encodeURIComponent(stateId));
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Could not load local governments (${response.status})`);
      }

      const lgas = await response.json();
      if (stateSelect.value !== stateId) {
        return;
      }

      lgaSelect.replaceChildren(new Option(lgas.length ? 'Select LGA' : 'No LGAs available', ''));
      lgas.forEach(lga => lgaSelect.add(new Option(lga.name, lga.id)));
      lgaSelect.disabled = lgas.length === 0;
    } catch (error) {
      if (stateSelect.value === stateId) {
        console.error('Failed to load local governments:', error);
        lgaSelect.replaceChildren(new Option('Could not load LGAs. Please try again.', ''));
        lgaSelect.disabled = true;
      }
    }
  });
});

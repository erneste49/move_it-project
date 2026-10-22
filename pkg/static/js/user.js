 const postStateSelect = document.getElementById('p_state');
    const postLgaSelect = document.getElementById('p_lga');

    postStateSelect.addEventListener('change', async function () {
        const stateId = this.value;
        postLgaSelect.replaceChildren();

        if (!stateId) {
            postLgaSelect.add(new Option('Select state first', ''));
            postLgaSelect.disabled = true;
            return;
        }

        postLgaSelect.add(new Option('Loading...', ''));
        postLgaSelect.disabled = true;

        try {
            const url = postStateSelect.dataset.lgaUrl.replace(/0$/, encodeURIComponent(stateId));
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Could not load local governments (${response.status})`);
            }

            const lgas = await response.json();
            if (postStateSelect.value !== stateId) {
                return;
            }

            postLgaSelect.replaceChildren(new Option(lgas.length ? 'Select LGA' : 'No LGAs available', ''));
            lgas.forEach(lga => postLgaSelect.add(new Option(lga.name, lga.id)));
        } catch (error) {
            if (postStateSelect.value === stateId) {
                console.error('Failed to load local governments:', error);
                postLgaSelect.replaceChildren(new Option('Could not load LGAs. Please try again.', ''));
            }
        } finally {
            if (postStateSelect.value === stateId) {
                postLgaSelect.disabled = false;
            }
        }
    });

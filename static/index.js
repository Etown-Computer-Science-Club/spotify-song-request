(function () {
	'use strict';

	window.addEventListener("load", init)

	function init() {
		const form = document.getElementById("addSongForm");
		form.addEventListener("submit", addToQueue);

		getAndSetQueue();
	}

	async function getAndSetQueue() {
		const response = await fetch("/api/queue");
		const queue = await response.json();

		const tbody = document.getElementById("currentQueueTBody");
		tbody.innerHTML = "";
		for (let song of queue) {
			console.log(song);
		}
	}

	async function addToQueue(event) {
		event.preventDefault();
		const form = event.target;

		const uriToAdd = form.uri.value;

		const response = await fetch("/api/queue",
			{
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ uri: uriToAdd })
			});

		console.log(response)
	}

})();
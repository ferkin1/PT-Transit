export const useUtils = () => {
    const sayHello = () => console.log('hello');

    async function fetchDestinations(origin: any) {
        let destinations = ref([]);
        const headers = new Headers();

        headers.append('Content-Type', 'application/json');
        headers.append('ngrok-skip-browser-warning', 'true');

        const res = await fetch(`http://localhost:8000/api/get-popular-travel?origin=` + origin, {
            method: "GET",
            headers: headers
        })
        destinations.value = await res.json();
        return destinations.value;
    }
    return { sayHello, fetchDestinations};
}
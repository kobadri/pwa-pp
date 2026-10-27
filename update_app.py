code = """document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menu-btn");
    const btnHariIni = document.getElementById("btn-hari-ini");
    const btnPekanIni = document.getElementById("btn-pekan-ini");
    const btnKaumBeriman = document.getElementById("btn-kaum-beriman");
    const dateText = document.getElementById("current-date-text");

    const today = new Date();
    
    const options = { weekday: "long", year: "numeric", month: "long", day: "numeric" };
    if (dateText) {
        dateText.textContent = today.toLocaleDateString("id-ID", options);
    }

    function getWeekAndDayInfo(targetDate) {
        const startDate = new Date(2026, 9, 5);
        const diffTime = targetDate - startDate;
        const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
        
        let weekNum = Math.floor(diffDays / 7) + 1;
        if (weekNum < 1) weekNum = 1;
        if (weekNum > 12) weekNum = 12;

        const daysMap = ["minggu", "senin", "selasa", "rabu", "kamis", "jumat", "sabtu"];
        let dayName = daysMap[targetDate.getDay()];
        if (dayName === "minggu") dayName = "senin";

        const weekStr = String(weekNum).padStart(2, "0");
        return { weekStr, dayName };
    }

    if (menuBtn) {
        menuBtn.addEventListener("click", () => {
            alert("Menu navigasi utama dibuka.");
        });
    }

    if (btnHariIni) {
        btnHariIni.addEventListener("click", () => {
            const { weekStr, dayName } = getWeekAndDayInfo(today);
            const targetPage = `data/teks/t_${weekStr}_${dayName}_01.html`;
            window.location.href = targetPage;
        });
    }

    if (btnPekanIni) {
        btnPekanIni.addEventListener("click", () => {
            alert("Membuka tampilan: Pekan Ini");
        });
    }

    if (btnKaumBeriman) {
        btnKaumBeriman.addEventListener("click", () => {
            alert("Membuka tampilan: Kaum Beriman");
        });
    }
});
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(code)
print("File app.js berhasil diperbarui dengan sempurna!")

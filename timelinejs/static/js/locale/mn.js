/* Mongolian LANGUAGE 
================================================== */
if(typeof VMM != 'undefined') {
	VMM.Language = {
		lang: "mn",
		api: {
			wikipedia: "mn"
		},
		date: {
		        month: ["Нэгдүгээр сар", "Хоёрдугаар сар", "Гуравдугаар сар", "Дөрөвдүгээр сар", "Тавдугаар сар", "Зургаадугаар сар", "Долдугаар сар", "Наймдугаар сар", "Есдүгээр сар", "Аравдугаар сар", "Арван нэгдүгээр сар", "Арван хоёрдугаар сар"],
		        month_abbr: ["1-р сар", "2-р сар", "3-р сар", "4-р сар", "5-р сар", "6-р сар", "7-р сар", "8-р сар", "9-р сар", "10-р сар", "11-р сар", "12-р сар"],
			day: ["Ням","Даваа", "Мягмар", "Лхагва", "Пүрэв", "Баасан", "Бямба"],
			day_abbr: ["Ня.","Да.", "Мя.", "Лх.", "Пү.", "Ба.", "Бя."]
		}, 
		dateformats: {
			year: "yyyy",
			month_short: "mmm",
			month: "yyyy оны mmmm",
			full_short: "mmm d",
		        full: "yyyy оны mmmmын d",
			time_no_seconds_short: "h:MM TT",
			time_no_seconds_small_date: "h:MM TT'<br/><small>'mmmm d',' yyyy'</small>'",
			full_long: "mmm d',' yyyy 'at' h:MM TT",
			full_long_small_date: "h:MM TT'<br/><small>mmm d',' yyyy'</small>'"
		},
		messages: {
			loading_timeline: "Цаглабар ачааллаж байна... ",
			return_to_title: "Эхлэл рүү буц",
			expand_timeline: "Цаглабарыг тэл",
			contract_timeline: "Цаглабарыг агшаа",
			wikipedia: "Чөлөөт нэвтэрхий толь Википэдиагаас",
			loading_content: "Мэдээллийг ачаалж байна",
			loading: "Ачааллаж байна"
		}
	}
}

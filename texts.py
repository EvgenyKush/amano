"""Все тексты интерфейса бота."""

from __future__ import annotations

from typing import Any

T: dict[str, dict[str, str]] = {
    "ru": {
        # Онбординг
        "welcome": (
            "Здравствуйте! Это «Квиты» — обмен умениями, где умениям нет цены.\n\n"
            "Час — не валюта, его нельзя копить. "
            "Закрыли обмен — вы квиты."
        ),
        "ask_name": "Как к вам обращаться? Напишите имя.",
        "name_too_short": "Имя слишком короткое. Напишите хотя бы 2 символа.",
        "ask_skills": (
            "В чём вы сильны? Выберите категории (от 1 до 5) или несколько раз «➕ Своё», "
            "затем нажмите «Готово»."
        ),
        "ask_skill_detail": "Что именно по {category}? Напишите одной фразой.",
        "skills_min": "Добавьте хотя бы одно умение — категорию или «➕ Своё».",
        "skills_max": "Максимум 5 умений. Снимите лишнее или нажмите «Готово».",
        "ask_needs": (
            "Что вам нужно? Выберите категории (от 1 до 3) или несколько раз «➕ Своё», "
            "затем «Готово»."
        ),
        "ask_need_detail": "Что именно нужно по {category}? Напишите одной фразой.",
        "needs_min": "Добавьте хотя бы одну потребность — категорию или «➕ Своё».",
        "needs_max": "Максимум 3 потребности.",
        "profile_card": (
            "Ваш профиль:\n\n"
            "👤 {name}\n"
            "💪 Умею: {skills}\n"
            "🎯 Нужно: {needs}\n\n"
            "Всё верно?"
        ),
        "registered": "Отлично, вы в системе! Команды: /people — участники, /deal — новая сделка, /me — профиль.",
        "already_registered": "Вы уже зарегистрированы. /me — ваш профиль.",

        # Профиль и реестр
        "my_profile": (
            "👤 {name}\n\n"
            "💪 Умею: {skills}\n"
            "🎯 Нужно: {needs}\n"
            "📊 Долги: {debts_count}/{debt_limit}\n"
            "✅ Закрытых сделок: {closed_deals}"
        ),
        "people_header": "Участники (стр. {page}/{total_pages}):",
        "people_item": "• {name} — {skills}",
        "people_empty": "Пока никого нет. Пригласите участников!",
        "find_usage": "Напишите: /find слово — поиск по умениям.",
        "find_results": "Нашли по «{query}»:",
        "find_empty": "По «{query}» никого не нашли. Попробуйте другое слово.",
        "find_item": "• {name} — {skills}",
        "paused": "Ваш профиль на паузе. Вы не участвуете в обменах.\n\nНажмите «Снять паузу», когда будете готовы вернуться.",
        "unpaused": "Снова в строю! Добро пожаловать обратно.",
        "pause_confirm": "Поставить профиль на паузу? Вас не будут видеть в реестре.",
        "edit_skills_start": "Обновим умения. Выберите категории (1–5), затем «Готово».",
        "edit_needs_start": "Обновим потребности. Выберите категории (1–3), затем «Готово».",
        "profile_updated": "Профиль обновлён.",

        # Сделки — создание
        "deal_choose_partner": "С кем обмен? Напишите имя или выберите из списка.",
        "deal_partner_not_found": "Участник не найден. Попробуйте другое имя или /people.",
        "deal_self": "Нельзя создать сделку с самим собой.",
        "deal_partner_paused": "Этот участник на паузе.",
        "deal_my_service": "Какую услугу вы предлагаете? Выберите из умений или напишите текстом.",
        "deal_my_hours": "Сколько часов займёт ваша услуга? Выберите или напишите число.",
        "deal_partner_service": "Какую услугу просите у партнёра? Напишите текстом.",
        "deal_partner_hours": "Сколько часов займёт услуга партнёра?",
        "deal_hours_invalid": "Укажите целое число от 1 до 20.",
        "deal_unequal_warning": (
            "Обмен неравный по времени ({hours_a} ч ⇄ {hours_b} ч) — "
            "ценность определяете вы, а не система. Продолжить?"
        ),
        "deal_sent": "Предложение отправлено {partner_name}. Ждём ответа.",
        "deal_proposal": (
            "🤝 {name} предлагает обмен:\n"
            "{service_a} · {hours_a} ч ⇄ {service_b} · {hours_b} ч"
        ),
        "deal_discuss_hint": "Свяжитесь с партнёром лично, обсудите детали и вернитесь к карточке.",
        "deal_rejected": "Предложение отклонено.",
        "deal_rejected_notify": "{name} отклонил(а) ваше предложение обмена.",
        "deal_accepted": "Сделка зафиксирована!",
        "deal_limit_blocked": (
            "Не можем зафиксировать сделку — лимит долгов.\n\n{details}"
        ),
        "deal_limit_detail": "• {name}: {count}/{limit} — {debts}",
        "deal_has_overdue": "У {name} есть просроченный долг. Сначала нужно его закрыть.",

        # Карточка сделки
        "deal_card": (
            "Сделка #{deal_id}\n"
            "Статус: {status_label}\n\n"
            "{side_a_name}: {service_a} · {hours_a} ч\n"
            "{side_b_name}: {service_b} · {hours_b} ч"
            "{safety_line}"
        ),
        "deal_safety_line": "\n\n🛡 Встречайтесь в публичных местах. До начала исполнения отмена свободная.",
        "deal_status_draft": "ожидает ответа",
        "deal_status_fixed": "зафиксирована",
        "deal_status_half_done": "одна услуга оказана",
        "deal_status_quits": "квиты ✓",
        "deal_status_cancelled": "отменена",
        "deal_status_annulled": "аннулирована",

        # Жизненный цикл сделки
        "deal_service_marked": "{name} отметил(а), что оказал(а) услугу. Подтвердите получение.",
        "deal_service_confirmed": "Услуга подтверждена. Долг зафиксирован до {deadline}.",
        "deal_both_done": "Обе услуги оказаны! Подтвердите «Мы квиты» и поставьте оценку.",
        "deal_quits_prompt": "🏁 Мы квиты? Подтвердите и оцените партнёра (★1–5).",
        "deal_quits_waiting": "Ждём подтверждения от партнёра.",
        "deal_quits_done": (
            "🎉 Квиты! Сделка #{deal_id} закрыта. Спасибо за обмен!"
        ),
        "deal_cancel_confirm": "Отменить сделку? Это действие нельзя отменить.",
        "deal_cancelled": "Сделка #{deal_id} отменена.",
        "deal_cancelled_notify": "{name} отменил(а) сделку #{deal_id}.",
        "deal_dispute_hint": (
            "Попробуйте договориться о доделке с партнёром. "
            "Если договориться не получится — можно оформить взаимную отмену."
        ),
        "deal_annul_confirm": "Взаимная отмена закроет сделку и долг. Точно?",
        "deal_annul_waiting": "Ждём подтверждения взаимной отмены от партнёра.",
        "deal_annulled": "Сделка #{deal_id} аннулирована по согласию сторон.",
        "deal_annulled_notify": "Сделка #{deal_id} аннулирована по взаимному согласию.",
        "deal_rating_saved": "Спасибо за оценку!",
        "deal_pending_confirm": "Ждём подтверждения получения услуги от партнёра.",
        "deal_already_done_side": "Вы уже отметили свою услугу. Ждём подтверждения партнёра.",

        # Список сделок
        "deals_header": "Ваши сделки:",
        "deals_empty": "Сделок пока нет. /deal — создать новую.",
        "deals_item": "#{deal_id} — {partner} — {status_label}",

        # Долги
        "debt_item": "• {service} для {creditor_name}, до {deadline}",
        "debt_reminder_3d": (
            "Дружеское напоминание: за вами {service} для {name}, до {deadline}."
        ),
        "debt_reminder_today": (
            "Сегодня дедлайн: {service} для {name}. Если нужна помощь — напишите консьержу."
        ),
        "debt_overdue_user": (
            "Долг просрочен: {service} для {name}. Новые сделки заблокированы до закрытия."
        ),
        "debt_overdue_concierge": (
            "⚠️ Просрочка: {debtor_name} должен {service} для {creditor_name} (сделка #{deal_id})."
        ),
        "draft_expired": "Сделка #{deal_id} автоматически отменена — 7 дней без ответа.",

        # Консьерж
        "concierge_only": "Эта команда только для консьержа.",
        "stats_report": (
            "📊 Сводка «Квиты»\n\n"
            "👥 Участников: {users_total} (активных: {users_active})\n"
            "🤝 Сделки: draft {draft}, fixed {fixed}, half_done {half_done}, "
            "quits {quits}, cancelled {cancelled}, annulled {annulled}\n"
            "💳 Долги: открыто {debts_open}, просрочено {debts_overdue}\n\n"
            "🔥 Топ-5 активных:\n{top_active}"
        ),
        "stats_top_item": "{i}. {name} — {deals_count} сделок",
        "stats_top_empty": "Пока нет данных.",
        "matches_header": "Пересечения «нужно ⇄ умею»:",
        "matches_empty": "Пересечений не нашли.",
        "matches_item": (
            "{mutual} {name_a} ({need_a} → {skill_b}) ⇄ "
            "{name_b} ({need_b} → {skill_a})"
        ),
        "match_intro_sent": "Знакомство отправлено обоим.",
        "match_intro_user": (
            "👋 Консьерж предлагает познакомиться!\n\n"
            "{name} умеет: {skills}\n"
            "Нужно: {needs}\n\n"
            "Возможный обмен: {hint}\n"
            "/deal — предложить сделку"
        ),
        "rings_header": "Кольца долгов (циклы из 3):",
        "rings_empty": "Колец не нашли.",
        "rings_item": "🔁 {name_a} → {name_b} → {name_c} → {name_a}",
        "ring_proposal_sent": "Предложение взаимозачёта отправлено троим.",
        "ring_proposal_user": (
            "🔄 Взаимозачёт: все три долга закроются разом.\n\n"
            "{name_a} → {name_b} → {name_c} → {name_a}\n\n"
            "Согласны?"
        ),
        "ring_proposal_waiting": "Ждём согласия остальных участников ({approved}/{total}).",
        "ring_proposal_done": "🎉 Взаимозачёт выполнен! Все три долга закрыты.",
        "export_done": "Выгрузка готова.",
        "broadcast_done": "Сообщение отправлено {count} участникам.",
        "broadcast_usage": "Напишите: /broadcast ваш текст",
        "pause_usage": "Напишите: /pause @username",
        "unpause_usage": "Напишите: /unpause @username",
        "user_paused_by_concierge": "Профиль {name} поставлен на паузу.",
        "user_unpaused_by_concierge": "Профиль {name} снова активен.",
        "user_not_found": "Участник не найден.",

        # Общие
        "confirm_yes": "Точно?",
        "btn_done": "✅ Готово",
        "btn_confirm": "✅ Да",
        "btn_cancel": "❌ Нет",
        "btn_all_correct": "✅ Всё верно",
        "btn_accept": "✅ Принять",
        "btn_discuss": "💬 Обсудить",
        "btn_reject": "❌ Отклонить",
        "btn_continue": "✅ Продолжить",
        "btn_my_service_done": "▶️ Я оказал(а) услугу",
        "btn_confirm_received": "✅ Подтверждаю, услугу получил(а)",
        "btn_quits": "🏁 Мы квиты",
        "btn_cancel_deal": "🚫 Отменить",
        "btn_dispute": "⚖️ Спор",
        "btn_mutual_annul": "Взаимная отмена",
        "btn_edit_skills": "✏️ Умения",
        "btn_edit_needs": "✏️ Потребности",
        "btn_pause": "⏸ Пауза",
        "btn_unpause": "▶️ Снять паузу",
        "btn_suggest_both": "Предложить обоим",
        "btn_suggest_offset": "Предложить зачёт",
        "btn_agree_offset": "✅ Согласен(на)",
        "error_generic": "Что-то пошло не так. Попробуйте ещё раз или напишите консьержу.",
        "error_not_found": "Не нашли. Возможно, уже удалено.",
        "error_no_access": "У вас нет доступа к этому действию.",
        "error_paused": "Ваш профиль на паузе. /me — снять паузу и вернуться.",
        "custom_category_prompt": (
            "Напишите своё умение или потребность одной фразой. "
            "Чтобы добавить ещё — снова нажмите «➕ Своё»."
        ),
        "custom_item_added": "Добавлено: «{title}». Ещё или нажмите «Готово».",
    },
}


def t(key: str, lang: str = "ru", **fmt: Any) -> str:
    """Получить локализованный текст по ключу."""
    texts = T.get(lang, T["ru"])
    template = texts.get(key, T["ru"].get(key, key))
    if fmt:
        return template.format(**fmt)
    return template


def status_label(status: str, lang: str = "ru") -> str:
    """Человекочитаемый статус сделки."""
    mapping = {
        "draft": "deal_status_draft",
        "fixed": "deal_status_fixed",
        "half_done": "deal_status_half_done",
        "quits": "deal_status_quits",
        "cancelled": "deal_status_cancelled",
        "annulled": "deal_status_annulled",
    }
    return t(mapping.get(status, "deal_status_draft"), lang)

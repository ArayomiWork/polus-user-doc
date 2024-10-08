Создание документации
=====================

Документация в приложении может формироваться на основе одной или нескольких форм.
В зависимости от типа формы, меняется набор формируемых документов:

#.  **Замечания**: журнал выдачи предписаний, отчёт о работе инженеров СК и предписание.
#.  **Приёмка работ**: отчёт о работе инженеров СК.
#.  **Испытания**: заявка на лабораторное испытание, отчёт о работе инженеров СК,
    отчёт о загруженности инженера лабораторного контроля в разрезе видов проведенных испытаний (сводный и ежемесячный),
    отчёт о загруженности инженера геодезического контроля в разрезе видов проведенных испытаний, реестр заявок на геодезические работы.
#.  **Входной контроль**: акт М7, акт входного контроля, журнал входного контроля, отчёт о работе инженеров СК.

Документация формируется однотипно, для примера рассмотрим формирование документов для **замечаний**.

Для создания документа на основе одного замечания, нажмите на форму правой кнопкой мыши и в контекстном меню выберите
"Сформировать документ".

..  thumbnail:: images/documents-creating-1-one-doc-creating.gif
    :alt: Создание документа на основе одной формы
    :align: center
    :title: Создание документа на основе одной формы
    :show_caption: True

Чтобы создать документ на основе нескольких замечаний,
вы можете выбрать конкретные замечания или нажать сочетание клавиш ``CTRL+A``, чтобы выбрать все.
После этого надо внизу нажать кнопку "Действия" или сочетание клавиш ``CTRL+K``. В появившемся меню выберите "Сформировать документ".

..  thumbnail:: images/documents-creating-2-multi-doc-creating.gif
    :alt: Создание документа на основе нескольких форм
    :align: center
    :title: Создание документа на основе нескольких форм
    :show_caption: True

После этого появится меню с вариантами документации. В случае с **замечаниями** оно будет выглядеть так:

..  thumbnail:: images/documents-creating-3-task-docs.png
    :alt: Типы документов для «замечаний»
    :width: 70%
    :title: Типы документов для «замечаний»
    :show_caption: True

Перед формирование документа необходимо заполнить форму из трёх полей: название документа, **номер документа**, **дата**, ---
последние два поля обязательны для заполнения.

..  thumbnail:: images/documents-creating-4-form-fill.png
    :alt: Заполнение формы для создания документа
    :width: 70%
    :title: Заполнение формы для создания документа
    :show_caption: True

После этого нажмите "Сформировать" и через некоторое время документ появится в разделе "Документооборот", в котором его можно скачать.
Подробнее об этом разделе можно почитать в соответствующей инструкции --- :doc:`document-flow`.

Фильтрация
----------

Чтобы формировать документацию было удобно, в приложении есть функция фильтрации форм.

Чтобы вызвать меню фильтров нажмите клавишу ``F`` или кнопку "Фильтр" в правом верхнем углу.

..  thumbnail:: images/documents-creating-5-filter-button.png
    :alt: Кнопка "Фильтр"
    :width: 30%
    :title: Кнопка "Фильтр"
    :show_caption: True

Для каждого типа формы идут свои собственные фильтры:

#.  **Замечания**: по статусу, по исполнителю, по ответственному, по виду работ, по сроку устранения, критичное и приостановка работ,
    --- последние два фильтра --- это чекбоксы, которые позволяют найти замечания, в которых поставлена критичность и/или из-за которых
    требуется приостановка работ.
#.  **Приёмка работ**: по статусу, по представителю генподрядчика, по представителю заказчика, по номеру акта, по виду работ.
#.  **Испытания**: по статусу, по типу испытаний, по исполнителю, по дате создания.
#.  **Входной контроль**: по статусу, по МТР, по участку, по организации поставщика, по материально-ответственному лицу, по инженеру ОВиСК.

Фильтрация для замечаний по статусу "Закрыто" будет выглядеть следующим образом:

..  thumbnail:: images/documents-creating-6-filtration.gif
    :alt: Фильтрация для замечаний
    :align: center
    :title: Фильтрация для замечаний
    :show_caption: True
CREATE TABLE IF NOT EXISTS preprocessed_texts
(
    "date" date NOT NULL,
    "url" text NOT NULL,
    "topic" text NOT NULL,
    "tags" text NOT NULL,
    "title" text NOT NULL,
    "texts" text NOT NULL,
    "text_str" text NOT NULL,
    "title_lemmas" text NOT NULL,
    "year" int NOT NULL,
    "month" int NOT NULL,
    "day" int NOT NULL,
    "date_enc" int NOT NULL,
    "day_of_week" int NOT NULL,
    "season" int NOT NULL,
    "dummy_weekday" int NOT NULL,
    "topic_le" text NOT NULL,
    "csv_name" text NOT NULL
);
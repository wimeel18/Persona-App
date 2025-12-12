import pandas as pd
from collections import Counter

from kivy.properties import ListProperty, DictProperty
from kivy.factory import Factory
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast


class QuizScreen(MDScreen):
    questions = ListProperty()
    answers = DictProperty({})
    page_size = 10
    current_page = 0  # mulai dari halaman 0



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_page = 0
        print("DEBUG: init QuizScreen")
        print("DEBUG: jumlah soal (awal) =", len(self.questions))

    def on_kv_post(self, base_widget):
        print("DEBUG: on_kv_post QuizScreen")
        self.load_questions()
        print("DEBUG: jumlah soal (setelah load) =", len(self.questions))
        self.build_all_questions()

    def load_questions(self):
        excel_path = r"kv/asset/excel/Daftar Pertanyaan Tes MBTI Copy.xlsx"
        df = pd.read_excel(excel_path)
        df = df.dropna(subset=["No", "Pertanyaan", "Golongan"])

        self.questions = []
        for _, row in df.iterrows():
            no = row["No"]
            if pd.isna(no):
                continue
            self.questions.append(
                {
                    "no": int(no),
                    "text": str(row["Pertanyaan"]),
                    "type": str(row["Golongan"]).strip(),   # 1 huruf: E/I/S/N/T/F/J/P
                    "reverse": int(row.get("Reverse", 0)),  # 0 atau 1
                }
            )


    def build_all_questions(self):
        print("DEBUG: build_all_questions dipanggil")
        #print("DEBUG ids:", self.ids.keys())
        container = self.ids.get("questions_container")
        if container is None:
            print("DEBUG: questions_container TIDAK ADA")
            return

        container.clear_widgets()

        # hitung batas soal untuk halaman ini
        start = self.current_page * self.page_size
        end = start + self.page_size
        page_questions = self.questions[start:end]  # HANYA 10 SOAL

        for q in page_questions:
            qb = Factory.QuestionBox()
            qb.no = q["no"]
            qb.question_text = q["text"]
            # kalau sebelumnya sudah ada jawaban, set selected_value
            existing = self.answers.get(q["no"])
            if existing:
                qb.selected_value = existing
            container.add_widget(qb)
            print("DEBUG: tambah soal", q["no"])

        container.height = container.minimum_height
        print("DEBUG: total widget di container =", len(container.children))

    #fungsi untuk cek semua soal di halaman sudah terjawab:
    def current_page_all_answered(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        page_questions = self.questions[start:end]
        for q in page_questions:
            if q["no"] not in self.answers:
                return False
        return True
    
    #fungsi next/prev:
    def go_next_page(self):
        if not self.current_page_all_answered():
            toast("Isi semua jawaban di halaman ini dulu.")
            return
        
        max_page = (len(self.questions) - 1) // self.page_size
        print("DEBUG max_page:", max_page)
        if self.current_page < max_page:
            self.current_page += 1
            print("DEBUG current_page:", self.current_page)
            self.build_all_questions()
        else:
            self.calculate_score()

    def go_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.build_all_questions()

    def set_answer(self, no_soal, value):
        if no_soal:
            self.answers[no_soal] = value
            # update tampilan QuestionBox yang sesuai
            #for child in self.ids.questions_container.children:
            #    if getattr(child, "no", None) == no_soal:
            #        child.selected_value = value
            #        break


    def calculate_score(self):
        from collections import Counter

        score = Counter({"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0})

        for q in self.questions:
            no = q["no"]
            if no not in self.answers:
                continue

            jawaban = self.answers[no]        # 1..5
            letter = q["type"]                # 'E','I',dst
            reverse = q.get("reverse", 0)

            if reverse:
                val = 6 - jawaban            # 1↔5, 2↔4
            else:
                val = jawaban - 1            # 0..4

            score[letter] += val

        ei = "E" if score["E"] >= score["I"] else "I"
        sn = "S" if score["S"] >= score["N"] else "N"
        tf = "T" if score["T"] >= score["F"] else "F"
        jp = "J" if score["J"] >= score["P"] else "P"
        mbti_type = ei + sn + tf + jp
        print("DEBUG score:", score)

        toast(f"Tipe MBTI kamu: {mbti_type}")

import unittest
from app import create_app


class TodoApiTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        })
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db = self.app.extensions["sqlalchemy"]
            db.session.remove()
            db.engine.dispose()

    def make(self, **values):
        data = {"text": "우유 사기", **values}
        return self.client.post("/api/todos/", json=data)

    def test_create_with_note_and_location(self):
        r = self.make(note="2리터짜리로")
        self.assertEqual(r.status_code, 201)
        data = r.get_json()
        self.assertEqual(data, {"id": data["id"], "text": "우유 사기",
                                "done": False, "note": "2리터짜리로"})
        self.assertEqual(r.headers["Location"], f'/api/todos/{data["id"]}')

    def test_list_without_filter_includes_both(self):
        a = self.make(done=True).get_json()
        b = self.make(text="책 반납").get_json()
        r = self.client.get("/api/todos/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual({x["id"] for x in r.get_json()}, {a["id"], b["id"]})

    def test_patch_preserves_omitted_fields(self):
        made = self.make(note="2리터짜리로").get_json()
        r = self.client.patch(f'/api/todos/{made["id"]}', json={"done": True})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json(), {**made, "done": True})

    def test_delete_then_get_returns_404(self):
        made = self.make().get_json()
        url = f'/api/todos/{made["id"]}'
        r = self.client.delete(url)
        self.assertEqual(r.status_code, 204)
        self.assertEqual(r.data, b"")
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_missing_id_returns_json_message(self):
        r = self.client.get('/api/todos/999')
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.get_json(), {"message": "999 번 할 일이 없습니다"})




if __name__ == "__main__":
    unittest.main()

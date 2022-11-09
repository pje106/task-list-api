from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    is_complete = db.Column(db.Boolean, default = False)

    def check_is_complete(self):
        if self.completed_at:
            return True
        else:
            return False 

    def to_dict(self):
        task_dict = {
        "id": self.task_id,
        "title": self.title,
        "description": self.description,
        "is_complete": self.check_is_complete()
        }
        
        return task_dict

    
    @classmethod
    def from_dict(cls, data_dict):
        if "title" in data_dict  and "description" in data_dict and "is_complete" in data_dict:
            new_obj = cls(
            title=data_dict["title"], 
            description=data_dict["description"], 
            is_complete=data_dict["is_complete"])
            
            return new_obj
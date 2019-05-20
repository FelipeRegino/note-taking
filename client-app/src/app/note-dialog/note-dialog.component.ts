import { Component } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material';
import { Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'note-dialog',
  templateUrl: 'note-dialog.html',
  styleUrls: ['./note.component.css']
})
export class NoteDialog {
  note = {
    'title' : '',
    'date': '',
    'content': ''
  };

  constructor(@Inject(MAT_DIALOG_DATA) public data: any, private http: HttpClient) { }

  ngOnInit() {
    if(this.data.note)
      this.note = this.data.note

  }

  deleteNote(){
    this.note.extra = "delete";
  }

  concludeNote(){
    this.note.extra = "conclude";
  }
}

import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatDialog } from '@angular/material';
import { NoteDialog } from './note-dialog/note-dialog.component'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Note Taking';
  notes = [];
  API_URL = 'http://localhost:5000'

  constructor(private http: HttpClient, public dialog: MatDialog) { }

  ngOnInit(){
    this.http.get(this.API_URL + '/get/notes')
      .subscribe((data) => {
        this.notes = data.notes;
      })
  }

  openDialog(note=null, action=false){
    const dialogRef = this.dialog.open(NoteDialog, {
      data: {
        note: note,
        action: action
      }
    });

    dialogRef.afterClosed().subscribe(data => {
      var d = new Date(data.date);
      data.date = this.formatDate(d);

      if(action){
        switch(data.extra){
          case 'delete':
            this.deleteNote(data)
            break;
          case 'conclude':
            data.status = !data.status;
            this.updateNote(data)
            break;
          default:
            this.updateNote(data)
        }
      }else{
        data.status = 1;
        this.createNote(data)
      }
    });
  }

  formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
  }

  createNote(data){
    this.http.post(this.API_URL + '/create/note/', data)
      .subscribe((data) => {
        this.notes.push(data.note)
      })
  }

  updateNote(data){
    this.http.put(this.API_URL + '/update/note/'+data.id, data)
      .subscribe((data) => {
      })
  }

  deleteNote(data){
    this.http.delete(this.API_URL + '/delete/note/'+data.id)
      .subscribe((data) => {
        this.ngOnInit()
      })
  }

}

import { NgModule } from '@angular/core';
import { MatDialogModule } from '@angular/material/dialog';
import { NoteDialog } from './note-dialog.component';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [NoteDialog],
  entryComponents: [NoteDialog],
  imports: [MatDialogModule,
            MatButtonModule,
            MatIconModule,
            MatInputModule,
            MatDatepickerModule,
            MatNativeDateModule,
            CommonModule],
  providers: [
    MatDatepickerModule,
  ],
  exports: [NoteDialog]
})
export class NoteDialogModule { }

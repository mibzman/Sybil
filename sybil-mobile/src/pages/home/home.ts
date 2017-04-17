import { Component } from '@angular/core';
import { NavController, 
	AlertController,
	ActionSheetController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController,) {
	}

}

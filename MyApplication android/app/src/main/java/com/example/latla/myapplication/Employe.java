package com.example.latla.myapplication;
import com.google.firebase.database.IgnoreExtraProperties;



@IgnoreExtraProperties
public class Employe {

     private String Nom;
     private String prenom;
     private String n_carte_rfid;
     private String mot_de_passe;

    public Employe() {
    }

    public Employe(String nom, String prenom, String n_carte_rfid, String mot_de_passe) {
        this.Nom = nom;
        this.prenom = prenom;
        this.n_carte_rfid = n_carte_rfid;
        this.mot_de_passe = mot_de_passe;
    }

    public String getNom() {
        return Nom;
    }

    public void setNom(String Nom) {
        this.Nom = Nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public String getN_carte_rfid() {
        return n_carte_rfid;
    }

    public void setN_carte_rfid(String n_carte_rfid) {
        this.n_carte_rfid = n_carte_rfid;
    }

    public String getMot_de_passe() {
        return mot_de_passe;
    }

    public void setMot_de_passe(String mot_de_passe) {
        this.mot_de_passe = mot_de_passe;
    }
}

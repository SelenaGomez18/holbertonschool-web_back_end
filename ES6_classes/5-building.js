export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Verifica si la clase hija implementa el método
    if (this.constructor !== Building) {
      if (typeof this.evacuationWarningMessage !== 'function') {
        throw new Error(
          'Class extending Building must override evacuationWarningMessage'
        );
      }
    }
  }

  // Getter
  get sqft() {
    return this._sqft;
  }
}

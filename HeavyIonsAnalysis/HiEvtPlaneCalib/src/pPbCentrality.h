#define pPbCentrality
const double pterrorpt_ = 0.05;
const Int_t CentNoffCut[19] = {100000, 350, 320, 300, 260, 240, 220, 185, 150, 120, 100, 80, 60, 50, 40, 30, 20, 10, 0};
//const Int_t CentNoffCut[] = {100000,         300, 260,      220, 185, 150, 120, 110, 90, 35, 0};
const Int_t nCentNoff = sizeof(CentNoffCut)/sizeof(Int_t);

TH1D * hNtrkoff;
  int Noffmin_;
  int Noffmax_;

int getNoffCent(const edm::Event& iEvent, const edm::EventSetup& iSetup, int& Noff)
{
  // very hard coded Noff track centrality cut
  using namespace edm;
  using namespace reco;
  //	int Noff = 0;
  
  Handle<VertexCollection> vertexCollection;
  iEvent.getByLabel(vtxCollection_, vertexCollection);
  const VertexCollection * recoVertices = vertexCollection.product();
  
  int primaryvtx = 0;
  math::XYZPoint v1( (*recoVertices)[primaryvtx].position().x(), (*recoVertices)[primaryvtx].position().y(), (*recoVertices)[primaryvtx].position().z() );
  double vxError = (*recoVertices)[primaryvtx].xError();
  double vyError = (*recoVertices)[primaryvtx].yError();
  double vzError = (*recoVertices)[primaryvtx].zError();
  
  
  Handle<TrackCollection> tracks;
  iEvent.getByLabel(trackCollection_,tracks);
  for(TrackCollection::const_iterator itTrack = tracks->begin();
      itTrack != tracks->end();                      
      ++itTrack) {
    
    if ( !itTrack->quality(reco::TrackBase::highPurity) ) continue;
    if ( itTrack->charge() == 0 ) continue;
    if ( itTrack->pt() < 0.4 ) continue;
    double d0 = -1.* itTrack->dxy(v1);
    double derror=sqrt(itTrack->dxyError()*itTrack->dxyError()+vxError*vyError);
    double dz=itTrack->dz(v1);
    double dzerror=sqrt(itTrack->dzError()*itTrack->dzError()+vzError*vzError);
    if ( fabs(itTrack->eta()) > 2.4 ) continue;
    if ( fabs( dz/dzerror ) > 3. ) continue;
    if ( fabs( d0/derror ) > 3. ) continue;
    if ( itTrack->ptError()/itTrack->pt() > pterrorpt_ ) continue;
    Noff++;
  }
  
  int cent = nCentNoff-1;
  while ( CentNoffCut[cent] <= Noff ) cent--;
  return cent;
}

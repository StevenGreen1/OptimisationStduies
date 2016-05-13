/**
 *  @file   PandoraAnalysis/include/AnalysisHelper.h
 * 
 *  @brief  Header file for the analysis helper class.
 * 
 *  $Log: $
 */

#ifndef ANALYSIS_HELPER_H
#define ANALYSIS_HELPER_H 1

class TH1F;

//------------------------------------------------------------------------------------------------------------------------------------------

namespace pandora_analysis
{

/**
 *  @brief  analysis helper class
 */
class AnalysisHelper
{
public:
    /**
     *  @brief  Calculate performance figures for an energy spectrum provided in form of a root th1f
     * 
     *  @param  pTH1F
     *  @param  fixDistributionCentre
     */
    static void CalculatePerformance(const TH1F *const pTH1F, bool fixDistributionCentre = true, const std::string &outputFileName = "results.txt");

    /**
     *  @brief  Calculate performance figures for an energy spectrum provided in form of a root th1f
     * 
     *  @param  pTH1F
     *  @param  resolution
     *  @param  resolutionError
     *  @param  fixDistributionCentre
     *  @param  print
     *  @param  outputFileName
     */
    static void CalculatePerformance(const TH1F *const pTH1F, float &resolution, float &resolutionError, bool fixDistributionCentre = true, bool print = true, const std::string &outputFileName = "results.txt");
};

//------------------------------------------------------------------------------------------------------------------------------------------

inline void AnalysisHelper::CalculatePerformance(const TH1F *const pTH1F, bool fixDistributionCentre, const std::string &outputFileName)
{
    float sigma(0.f), sigmasigma(0.f);
    return CalculatePerformance(pTH1F, sigma, sigmasigma, fixDistributionCentre, true, outputFileName);
}

} // namespace pandora_analysis

#endif // #ifndef ANALYSIS_HELPER_H
